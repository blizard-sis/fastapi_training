from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class PrompterHint(BaseModel):
    actor: str
    replica: str

    class Config:
        schema_extra = {
            'examples': {
                'coloboc': {
                    'summary': 'Колобок',
                    'value': {
                       'actor': 'Медведь',
                       'replica': 'Колобок, колобок, я тебя съем!',
                    }
                },
                'gamlet': {
                    'summary': 'Гамлет, принц датский',
                    'value': {
                       'actor': 'Гамлет',
                       'replica': 'Бедный Йорик! Я знал его, Горацио.',
                    }
                },
                'palata6': {
                    'summary': 'Палата номер 6',
                    'value': {
                        'actor': 'Рагин',
                        'replica': 'Покой и довольство человека не вне его, а в нём самом.',
                    }
                }
            }
        }


@app.post('/give-a-hint')
def send_prompt(
    hint: PrompterHint = Body(
            ..., examples=PrompterHint.Config.schema_extra['examples']
    )
):
    return hint
