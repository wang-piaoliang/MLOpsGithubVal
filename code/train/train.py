from azureml.pipeline.core import PipelineEndpoint
from azureml.core import Workspace
from azureml.core.authentication import ServicePrincipalAuthentication
from azureml.core.authentication import AzureCliAuthentication
import os

from azureml.core import Run
run = Run.get_context()
ws = run.experiment.workspace

    
published_pipeline = PipelineEndpoint.get(workspace=ws, name="aml-run-regression")
print(published_pipeline)

print("submitting pipeline aml-run-val")
pipeline_run = published_pipeline.submit("github-val-yueyue")
print("pipeline aml-run-val run completed")




