import bentoml
from bentoml.io import JSON
from pydantic import BaseModel


class AgeMarriageApplication(BaseModel):
    gender: str
    height: float
    religion: str
    caste: str
    mother_tongue: str

model_ref = bentoml.sklearn.get("marriage_model:6o3yllsqo6g4oq4n")

dv = model_ref.custom_objects["dictVectorizer"]

# get access to the model
model_runner = model_ref.to_runner()

# create a service
svc = bentoml.Service("marriage_regressor", runners=[model_runner])

@svc.api(input=JSON(pydantic_model=AgeMarriageApplication), output=JSON())
async def classify(marriage_application):
    application_data = marriage_application.dict()
    vector = dv.transform(application_data)
    prediction = await model_runner.predict.async_run(vector)
    # print(prediction)
    result = prediction[0]

    return {"Age": round(result)}
    