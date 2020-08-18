import logging
import traceback

from certbot import crypto_util
from certbot._internal.cert_manager import certificates 
from certbot._internal import configuration
from certbot._internal import cli
from certbot._internal.plugins import disco as plugins_disco
from certbot._internal import storage
from . import constants
logger = logging.getLogger(__name__)

def list_certificates():
    """Display information about certs configured with Certbot

    :param config: Configuration.
    :type config: :class:`certbot._internal.configuration.NamespaceConfig`
    """
    
    plugins = plugins_disco.PluginsRegistry.find_all()
    
    args = cli.prepare_and_parse_args(plugins, [
        "certificates", 
        "--config-dir=" + constants.CONFIG_DIR, 
        "--work-dir=" + constants.WORK_DIR, 
        "--logs=" + constants.LOGS_DIR
    ])
    config = configuration.NamespaceConfig(args)
    
    parsed_certs = []
    parse_failures = []
    for renewal_file in storage.renewal_conf_files(config):
        try:
            renewal_candidate = storage.RenewableCert(renewal_file, config)
            crypto_util.verify_renewable_cert(renewal_candidate)
            parsed_certs.append(renewal_candidate)
        except Exception as e:  # pylint: disable=broad-except
            logger.warning("Renewal configuration file %s produced an "
                           "unexpected error: %s. Skipping.", renewal_file, e)
            logger.debug("Traceback was:\n%s", traceback.format_exc())
            parse_failures.append(renewal_file)
    
    return (parsed_certs, parse_failures)