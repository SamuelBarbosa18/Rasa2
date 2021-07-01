from rasa_sdk.forms import FormValidationAction
from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class ValidateFormSaude(FormValidationAction):
    def name(self) -> Text:
        return "ValidateFormSaude"

    async def validate_confirmar_exercicio(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if value:
            return {"confirmar_exercicio": True}
        else:
            return {"exercicio": "None", "confirmar_exercicio": False }