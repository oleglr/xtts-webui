import gradio as gr
from xtts_webui import *

from scripts.rvc_scripts import find_rvc_model_by_name,get_rvc_models

def select_rvc_model(rvc_settings_model_name):
  mode_path,index_path = find_rvc_model_by_name(this_dir,rvc_settings_model_name)

  # print(mode_path,index_path)
  if mode_path:
    return mode_path,index_path


def update_rvc_model(rvc_settings_model_name):
  rvc_models_new = []
  rvc_models_full = get_rvc_models(this_dir)
  if len(rvc_models_full) == 0:
    return gr.Dropdown(label="RVC Model name",info="Create a folder with your model name in the rvc folder and put .pth and .index there , .index optional",choices=[],value=""),"",""
  
  for model in rvc_models_full:
    rvc_models_new.append(model["model_name"])
  
  model_name = rvc_models_new[0]
  model_path,index_path = find_rvc_model_by_name(this_dir,model_name)

  return gr.Dropdown(label="RVC Model name",info="Create a folder with your model name in the rvc folder and put .pth and .index there , .index optional",choices=rvc_models_new,value=model_name),model_path,index_path
  
rvc_settings_model_name.change(fn=select_rvc_model,inputs=[rvc_settings_model_name],outputs=[rvc_settings_model_path,rvc_settings_index_path])
rvc_settings_update_btn.click(fn=update_rvc_model,inputs=[rvc_settings_model_name],outputs=[rvc_settings_model_name,rvc_settings_model_path,rvc_settings_index_path])