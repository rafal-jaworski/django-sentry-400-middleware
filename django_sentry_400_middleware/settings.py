from django.conf import settings


IGNORED_USER_AGENTS = getattr(settings, 'SENTRY_404_IGNORED_USER_AGENTS', [])
PROCESS_REQUEST_POST_DATA = getattr(settings, 'SENTRY_404_PROCESS_REQUEST_POST_DATA', True)
