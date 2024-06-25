import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from diffusers import StableDiffusionPipeline
from io import BytesIO

# Charger le modèle Hugging Face
model_name = "hf-internal-testing/tiny-stable-diffusion-torch"
pipe = StableDiffusionPipeline.from_pretrained(model_name)


# Créer l'application Tkinter
class ImageGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Generator App")

        # Créer une zone de texte pour saisir la description
        self.prompt_label = tk.Label(root, text="Enter a description:")
        self.prompt_label.pack()
        self.prompt_entry = tk.Entry(root, width=50)
        self.prompt_entry.pack()

        # Créer un bouton pour générer l'image
        self.generate_button = tk.Button(root, text="Generate Image", command=self.generate_image)
        self.generate_button.pack()

        # Créer un indicateur de chargement (spinner)
        self.spinner = ttk.Progressbar(root, mode='indeterminate')

        # Créer une zone d'affichage pour montrer l'image générée avec la légende
        self.image_label = tk.Label(root)
        self.image_label.pack()
        self.caption_label = tk.Label(root, text="")
        self.caption_label.pack()

    def generate_image(self):
        prompt = self.prompt_entry.get()
        if not prompt:
            return

        # Afficher le spinner pendant la génération de l'image
        self.spinner.pack()
        self.spinner.start()

        # Générer l'image en utilisant le modèle Hugging Face
        self.root.after(100, self.run_generation, prompt)

    def run_generation(self, prompt):
        try:
            image = pipe(prompt).images[0]
            # Convertir l'image pour l'afficher dans Tkinter
            image_bytes = BytesIO()
            image.save(image_bytes, format='PNG')
            image_bytes.seek(0)
            pil_image = Image.open(image_bytes)
            tk_image = ImageTk.PhotoImage(pil_image)

            # Afficher l'image générée
            self.image_label.config(image=tk_image)
            self.image_label.image = tk_image

            # Mettre à jour la légende
            self.caption_label.config(text=prompt)
        finally:
            # Arrêter le spinner après la génération de l'image
            self.spinner.stop()
            self.spinner.pack_forget()


# Créer l'instance de l'application Tkinter
root = tk.Tk()
app = ImageGeneratorApp(root)
root.mainloop()
