import torch
from nnunetv2.training.nnUNetTrainer.nnUNetTrainer import nnUNetTrainer

class nnUNetTrainer_500epochs(nnUNetTrainer):
    def __init__(self, plans, configuration, fold, dataset_json, device=torch.device('cuda')):
        # 严格匹配你本地 nnU-Net 版本的参数列表
        super().__init__(plans, configuration, fold, dataset_json, device)
        
        # 核心修改：锁定 500 轮
        self.num_epochs = 500
