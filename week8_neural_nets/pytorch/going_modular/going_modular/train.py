import os
import torch
from pathlib import Path
from torchvision import transforms

# Import modular scripts
import data_setup, engine, model_builder, utils

def main():
    # 1. Setup Hyperparameters
    NUM_EPOCHS = 5
    BATCH_SIZE = 32
    HIDDEN_UNITS = 10
    LEARNING_RATE = 0.001
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    # 2. Robust Path Handling
    # This finds the directory where train.py lives, then goes up one level to find 'data'
    base_path = Path(__file__).resolve().parent.parent
    train_dir = base_path / "data" / "pizza_steak_sushi" / "train"
    test_dir = base_path / "data" / "pizza_steak_sushi" / "test"

    print(f"[INFO] Using data from: {base_path / 'data'}")
    print(f"[INFO] Training on device: {device}")

    # 3. Create Transforms
    data_transform = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.ToTensor()
    ])

    # 4. Create DataLoaders
    train_dataloader, test_dataloader, class_names = data_setup.create_dataloaders(
        train_dir=str(train_dir),
        test_dir=str(test_dir),
        transform=data_transform,
        batch_size=BATCH_SIZE
    )

    # 5. Build Model
    model = model_builder.TinyVGG(
        input_shape=3,
        hidden_units=HIDDEN_UNITS,
        output_shape=len(class_names)
    ).to(device)

    # 6. Setup Loss and Optimizer
    loss_fn = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

    # 7. Start Training
    engine.train(model=model,
                 train_dataloader=train_dataloader,
                 test_dataloader=test_dataloader,
                 loss_fn=loss_fn,
                 optimizer=optimizer,
                 epochs=NUM_EPOCHS,
                 device=device)

    # 8. Save the model
    utils.save_model(model=model,
                     target_dir="models",
                     model_name="05_going_modular_script_mode_tinyvgg_model.pth")

# The critical "Windows Fix" guard
if __name__ == "__main__":
    main()