
# app.py
import gradio as gr
from environment import SmartFactoryEnv

# Initialize the environment
env = SmartFactoryEnv()

def reset_env():
    state = env.reset()
    return str(state)

def step_env(machine, task):
    action = {"machine": machine, "task": task}
    result = env.step(action)
    return str(result)

with gr.Blocks() as demo:
    gr.Markdown("# Smart Factory Environment 🚀")
    
    # Output textbox component
    output_text = gr.Textbox(label="Environment Output", lines=10)
    
    # Reset button
    reset_btn = gr.Button("Reset Environment")
    reset_btn.click(reset_env, outputs=output_text)
    
    # Step controls
    machine_input = gr.Dropdown(["M1", "M2", "M3"], label="Select Machine")
    task_input = gr.Dropdown(["process_raw"], label="Select Task")
    step_btn = gr.Button("Take Step")
    step_btn.click(step_env, inputs=[machine_input, task_input], outputs=output_text)

demo.launch()