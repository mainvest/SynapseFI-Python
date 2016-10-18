from .base_node import BaseNode


class WireUsNode(BaseNode):
    """Represents a WIRE-US node
    """

    @classmethod
    def payload_for_create(cls, nickname, bank_name, account_number,
                           name_on_account, address, **kwargs):
        payload = super().payload_for_create('WIRE-US', nickname,
                                             bank_name=bank_name,
                                             account_number=account_number,
                                             name_on_account=name_on_account,
                                             address=address,
                                             **kwargs)
        return payload
