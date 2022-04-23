import torch

def freeze_model(model):
    for param in model.parameters():
        param.requires_grad = False

def new_classification_layer(model, n_classes):
    embedding_size = model.fc.in_features
    model.fc = torch.nn.Linear(embedding_size, n_classes)
    return model