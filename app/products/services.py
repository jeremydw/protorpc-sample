from protorpc import remote
from protorpc import messages


class PersonMessage(messages.Message):
    name = messages.StringField(1)


class SayHelloRequest(messages.Message):
    person = messages.MessageField(PersonMessage, 1, required=True)


class SayHelloResponse(messages.Message):
    speech_bubble = messages.StringField(1)


class ProductService(remote.Service):

    @remote.method(SayHelloRequest,
                   SayHelloResponse)
    def say_hello(self, request):
        person = request.person
        speech_bubble = 'Hello, {}!'.format(person.name)
        resp = SayHelloResponse()
        resp.speech_bubble = speech_bubble
        return resp
