
# broomba bot



## Основные источники информации

[Учебник от легенды mastergroosha](https://mastergroosha.github.io/aiogram-3-guide/)

[Документация aiogram3](https://docs.aiogram.dev/en/v3.17.0/)


## Установка и настройка виртуального окружения
#### Клонируем репозиторий

```bash
git install https://github.com/goingbraindeadisolated/broombabot.git
cd my-project
```
#### Устанавливаем виртуальное окружение и необходимые зависимости (Linux/MacOS)
```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```
## Настраиваем SSH-соединение (чтобы git push и git pull не требовали авторизацию)

#### Создаем SSH-ключ (если его нет):
   ```bash
   ssh-keygen -t ed25519
   ```
   Нажмите Enter для значений по умолчанию.



####   Копируем и вставляем в [GitHub SSH Keys](https://github.com/settings/keys):
   
    cat ~/.ssh/id_ed25519.pub.

#### Проверяем подключение:
   ```bash
   ssh -T git@github.com
   ```
   Должно появиться: `Hi username! You've successfully authenticated...`

#### Подключаем репозиторий: 
    git remote set-url origin git@github.com:goingbraindeadisolated/broombabot.git
