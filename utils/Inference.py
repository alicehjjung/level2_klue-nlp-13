import os
import wandb
import pandas as pd
import pickle as pickle
import pytorch_lightning as pl
import torch
from utils.Model import Model
from utils.R_RoBERTa_model import RRoBERTa
from utils.DataLoader import DataLoader
from utils.Utils import *
from pytorch_lightning.loggers import WandbLogger



def inference(cfg):
    save_path, folder_name = cfg['save_path'], cfg['folder_name']
    #save_path = './results/2023-05-17-12:00:56_박지연'
    #folder_name = '2023-05-17-12:00:56_박지연'
    dataloader = DataLoader(cfg['model']['model_name'],
                            cfg['model']['batch_size'],
                            cfg['model']['max_len'],
                            cfg['model']['multi_sen'],
                            cfg['model']['shuffle'])

    wandb_logger = WandbLogger(save_dir=save_path)
    trainer = pl.Trainer(accelerator="auto", logger=wandb_logger)
    #trainer = pl.Trainer(accelerator="auto")

    model = torch.load(f'{save_path}/{folder_name}_model.pt')
    predicts = trainer.predict(model, datamodule=dataloader)

    pred, prob = get_result(predicts)
    pred = num_to_label(pred)

    output = pd.DataFrame({'id':[i for i in range(len(pred))],'pred_label':pred,'probs':prob})
    print(output)
    #output.to_csv(f'{folder_name}_predict.csv', index=False)
    output.to_csv(f'{save_path}/{folder_name}_predict.csv', index=False)