import torch
import model.lora.lora as lora
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

def generate_pic(prompt:str):
    prompt= prompt
    device = "cuda"
    lora_path = "SVG.safetensors"
    base_model = "jianghushinian/animefull-final-pruned"
    generator = torch.Generator(device=device)
    seed = generator.seed()

    pipe = StableDiffusionPipeline.from_pretrained(base_model, 
        torch_dtype=torch.float16,
        # safety_checker = None,
    )
    
    # pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    
    pipe.enable_xformers_memory_efficient_attention()
    # pipe.set_scheduler('sample_dpmpp_2m')
    pipe.to(device)

    pipe = lora.load_lora_weights(pipe, lora_path, 1.0, 'cuda', torch.float16)

    image = pipe(prompt=prompt,
        num_inference_steps=32, generator=torch.Generator(device=device).manual_seed(seed), 
        width=512, height=512).images[0]
    
    return image
