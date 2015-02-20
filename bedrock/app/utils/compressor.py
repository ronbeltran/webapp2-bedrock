import os

from webassets.loaders import YAMLLoader
import config

ASSETS_PATH = os.path.join(config.PROJECT_ROOT, 'webassets.yaml')

loader = YAMLLoader(ASSETS_PATH)
WEBASSETS_ENV = loader.load_environment()

if os.environ.get('SERVER_SOFTWARE') == 'Development/2.0':
    # running on dev_appserver, don't use compiled assets
    WEBASSETS_ENV.debug = False
