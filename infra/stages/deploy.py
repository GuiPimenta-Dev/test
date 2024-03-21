from functions.somewhere.hello_world.config import HelloWorldConfig
from functions.authorizers.docs.config import DocsConfig
import aws_cdk as cdk
from constructs import Construct
from infra.services import Services
from lambda_forge import release, LambdaStack


@release
class DeployStage(cdk.Stage):
    def __init__(self, scope: Construct, context, **kwargs):
        super().__init__(scope, context.stage, **kwargs)

        services = Services(scope, context)

        authorizers = []

        functions = [
            HelloWorldConfig(services),
        ]

        LambdaStack(
            self,
            context=context,
            services=services,
            authorizers=authorizers,
            functions=functions,
            docs=True,
            docs_authorizer=None,
        )
