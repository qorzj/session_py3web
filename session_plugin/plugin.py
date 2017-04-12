import web
from web import config, ctx

__all__ = ["set_content_to_token", "set_token_to_content", "become", "create_session"]


def set_content_to_token(content_to_token_func):
    web.g.session_content_to_token_func = content_to_token_func


def set_token_to_content(token_to_content_func):
    web.g.session_token_to_content_func = token_to_content_func


def become(token=None):
    """
    token = session_plugin.create_session(content)
    content = session_plugin.become()
    content = session_plugin.become(token)
    """
    if token is None and 'cookie_name' in config.session:
        try: token = web.cookie().get(config.session.cookie_name)
        except: pass
    if token is None and 'header_name' in config.session:
        token = web.ctx.env.get('HTTP_' + config.session.header_name.upper())
    if token is None:
        return None
    return web.g.session_token_to_content_func(token)


def create_session(content):
    token = web.g.session_content_to_token_func(content)
    if 'cookie_name' in config.session:
        web.setcookie(config.session.cookie_name, token, **config.session.cookie_setting) if \
                'cookie_setting' in config.session else web.setcookie(config.session.cookie_name, token)

    return token

