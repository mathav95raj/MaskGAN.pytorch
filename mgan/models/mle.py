
from fairseq.models.lstm \
        import LSTMEncoder, \
               LSTMDecoder, \
               LSTMModel

from fairseq.models.fairseq_model \
        import FairseqModel

from warnings import warn

class MLEEncoder(LSTMEncoder): pass
class MLEDecoder(LSTMDecoder): pass
class MaskedMLE(LSTMModel): 
    def forward(self, *args, **kwargs):
        self.encoder.lstm.flatten_parameters()
        #self.decoder.lstm.flatten_parameters()
        return super().forward(*args, **kwargs)


