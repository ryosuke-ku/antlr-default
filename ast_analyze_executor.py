import logging.config
from ast.ast_processor import AstProcessor
from ast.basic_info_listener import BasicInfoListener


if __name__ == '__main__':
    target_file_path = '解析対象のファイルパス'

    # ★ポイント１
    ast_info = AstProcessor(None, BasicInfoListener()).execute(target_file_path)