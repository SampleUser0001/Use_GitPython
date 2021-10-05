# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os

import sys
from logutil import LogUtil
from importenv import ImportEnvKeyEnum
import importenv as setting

import git

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(PYTHON_APP_HOME + '/config/log_config.json')
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

if __name__ == '__main__':
  # .envの取得
  # setting.ENV_DIC[ImportEnvKeyEnum.importenvに書いた値.value]
  
  # 起動引数の取得
  # args = sys.argv
  # args[0]はpythonのファイル名。
  # 実際の引数はargs[1]から。

  # urlは適宜自身が編集可能なレポジトリに書き換えてください
  url = setting.ENV_DIC[ImportEnvKeyEnum.GIT_REPOSITORY_URL.value]
  
  # cloneしたプロジェクトを出力するパス
  to_path = PYTHON_APP_HOME + '/repo/' + setting.ENV_DIC[ImportEnvKeyEnum.GIT_DIRECTORY.value]
  
  git.Repo.clone_from(
      url,
      to_path)  
