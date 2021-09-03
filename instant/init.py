from typing import Any, Dict, List, Union


from django.conf import settings


def generate_settings_from_conf(
    conf: Dict[str, Any], site_name: Union[str, None] = None
) -> List[str]:
    """
    Generate Django settings from Centrifugo json conf
    """
    buffer = []
    buffer.append('CENTRIFUGO_HOST = "http://localhost"')
    buffer.append("CENTRIFUGO_PORT = 8427")
    buffer.append(f'CENTRIFUGO_HMAC_KEY = "{conf["token_hmac_secret_key"]}"')
    buffer.append(f'CENTRIFUGO_API_KEY = "{conf["api_key"]}"')
    project_name = settings.BASE_DIR.name
    if site_name is not None:
        project_name = site_name
    buffer.append(f'SITE_NAME = "{project_name}"')
    return buffer


def ensure_channel_is_private(chan):
    """
    Make sure that a private channel name starts with a $ sign
    """
    name = chan
    if ":" in name:
        names = name.split(":")
        prefix = names[0]
        suffix = names[1]
        if suffix.startswith("$") is False:
            return prefix + ":$" + suffix
    else:
        if chan.startswith("$") is False:
            return "$" + chan
    return chan
