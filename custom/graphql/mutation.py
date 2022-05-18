import graphene

from saleor.graphql.core.mutations import ModelMutation, ModelDeleteMutation
from .customError import CustomError
from custom import models
from .types import Custom


class CustomInput(graphene.InputObjectType):
    name = graphene.String(description="Custom name")
    age = graphene.String(description="Custom age")
    attribute = graphene.String(description="Custom attribute")


class CustomCreate(ModelMutation):
    class Arguments:
        input = CustomInput(required=True,
                            description="Fields required to create custom")

    class Meta:
        description = "Creates new custom."
        model = models.Custom
        error_type_class = CustomError
        error_type_field = "custom_errors"

    @classmethod
    def get_type_for_model(cls):
        return Custom

    @classmethod
    def perform_mutation(cls, _root, info, **data):
        custom = super().perform_mutation(_root, info, **data)

        return custom

class CustomUpdate(ModelMutation):
    class Arguments:
        id = graphene.ID(description="ID of a custom update.", required=True)
        input = CustomInput(required=True,
                            description="Fields required to create custom.")

    class Meta:
        description = "Creates new custom."
        model = models.Custom
        error_type_class = CustomError
        error_type_field = "custom_errors"



class CustomDelete(ModelDeleteMutation):
    class Arguments:
        id = graphene.ID()

    class Meta:
        description = "Delete the custom."
        model = models.Custom
        error_type_class = CustomError
        error_type_field = "custom_errors"
