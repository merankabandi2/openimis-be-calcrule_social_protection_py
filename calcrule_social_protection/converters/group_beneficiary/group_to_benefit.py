from calcrule_social_protection.converters.builder import BuilderToBenefitConverter
from individual.models import GroupIndividual


class GroupToBenefitConverter(BuilderToBenefitConverter):

    @classmethod
    def _build_individual(cls, benefit, entity):
        group_recipient = GroupIndividual.objects.filter(
            group_id=entity.group.id,
            role=GroupIndividual.RecipientType.PRIMARY.value,
            is_deleted=False
        ).first()
        if group_recipient:
            benefit["individual_id"] = f"{group_recipient.individual.id}"
            return
        group_recipient = GroupIndividual.objects.filter(
            group_id=entity.group.id,
            role=GroupIndividual.Role.HEAD.value,
            is_deleted=False
        ).first()
        if group_recipient:
            benefit["individual_id"] = f"{group_recipient.individual.id}"
            return
        group_recipient = GroupIndividual.objects.filter(
            group_id=entity.group.id,
            is_deleted=False
        ).first()
        if group_recipient:
            benefit["individual_id"] = f"{group_recipient.individual.id}"
        
