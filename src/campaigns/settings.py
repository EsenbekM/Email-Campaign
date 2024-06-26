
class SentStatus:
    pending = 'pending'
    sent = 'sent'
    failed = 'failed'

    @classmethod
    def choices(cls):
        return [
            (cls.pending, 'Pending'),
            (cls.sent, 'Sent'),
            (cls.failed, 'Failed'),
        ]

    @classmethod
    def all(cls):
        return [cls.pending, cls.sent, cls.failed]