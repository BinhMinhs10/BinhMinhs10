#!/bin/bash

echo "Activate exenv enviroment!"

source /media/user/Extensions/source_Python/exenv/bin/activate
conda deactivate

echo "Deactivate exenv enviroment"
deactivate
