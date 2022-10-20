import bentoml
from bentoml.io import JSON
from bentoml.io import NumpyNdarray
from pydantic import BaseModel


class UserProfile(BaseModel):
    name: str
    age: int
    country: str
    rating: float

model_ref = bentoml.sklearn.get("mlzoomcamp_homework:latest")

# get access to the model
model_runner = model_ref.to_runner()

# create a service
svc = bentoml.Service("zoomcamp_risk_classifier", runners=[model_runner])

@svc.api(input=NumpyNdarray(), output=JSON())
async def classify(credit_application):
    # application_data = credit_application.dict()
    # vector = dv.transform(application_data)
    prediction = await model_runner.predict.async_run(credit_application)
    print(prediction)
    return {"Pred": prediction}
    