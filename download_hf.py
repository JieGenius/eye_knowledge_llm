import os
from modelscope import snapshot_download, AutoModel, AutoTokenizer

# 设置环境变量
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

def download():
# 下载模型
    os.system('huggingface-cli download --resume-download sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 --local-dir model/sentence-transformer')

def download_model(model_path):
    model_dir = snapshot_download('Shanghai_AI_Laboratory/internlm-chat-7b', cache_dir=model_path, revision='v1.0.3')
