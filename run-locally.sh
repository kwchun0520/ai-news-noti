#usr/zsh
export $(cat .env | xargs)
pdm run python main.py