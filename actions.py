from rasa_core_sdk import Action
from google.cloud import automl

project = 'aerobic-cosmos-271904'

class ActionGetClassification(Action):

    def name(self):
        return 'action_get_classification'

    def run(self, dispatcher, tracker, domain):

        uri = tracker.get_slot('document_uri')

        gcssource = automl.types.GcsSource(input_uris=uri)
        documentconfig = automl.types.DocumentInputConfig(gcs_source=gcssource)
        document = automl.types.Document(input_config=documentconfig)

        payload = automl.types.ExamplePayload(document=document)

        response = prediction_client.predict(model_full_id, payload)

        for annotation_payload in response.payload:
            print(
                u"Predicted class name: {}".format(annotation_payload.display_name)
            )
            print(
                u"Predicted class score: {}".format(
                    annotation_payload.classification.score
                )
            )

            message = "I'm %s sure this is a %s" %(annotation_payload.classification.score, annotation_payload.display_name)

            dispatcher.utter_message(message)

        return []
