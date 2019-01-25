## TODO: define the convolutional neural network architecture

import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self, num_classes=10):
        super(Net, self).__init__()
        
        # Convolution Layers
        self.conv1 = nn.Conv2d(1, 32, 3)
        self.conv2 = nn.Conv2d(32, 64, 3)
        self.conv3 = nn.Conv2d(64, 128, 3)
        self.conv4 = nn.Conv2d(128, 64, 3)
        self.conv5 = nn.Conv2d(64, 32, 3)
        
        # Maxpooling Layers
        self.pool = nn.MaxPool2d(2, 2)
        
        # Fully Connected Layers
        self.fc1 = nn.Linear(128,64)
        self.fc2 = nn.Linear(64, num_classes)
        
        # Dropout Layers
        self.drop = nn.Dropout(0.8)
        
    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.pool(x)
        x = self.drop(x)
        
        x = self.pool(F.relu(self.conv2(x)))
        #x = self.drop(x)
        x = self.pool(F.relu(self.conv3(x)))
        #x = self.drop(x)
        x = self.pool(F.relu(self.conv4(x)))
        #x = self.drop(x)
        x = self.pool(F.relu(self.conv5(x)))
       
        
        x = x.view(x.size(0), -1)
        
        x = self.drop(F.relu(self.fc1(x)))
        x = self.fc2(x)
        x = F.log_softmax(x, dim=1)
        return x