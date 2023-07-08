from typing import Optional
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry import trace

from prometheus_fastapi_instrumentator import Instrumentator
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor


def init_instrumentation(app, service_name: str, otlp_exporter_url: str):
    exporter = OTLPSpanExporter(endpoint=otlp_exporter_url, insecure=True)

    resource = Resource.create(
        attributes={
            SERVICE_NAME: service_name,
            "developer": "Rafael",  # get that from env var
            "environment": "dev",  # get that from env var
        }
    )
    provider = TracerProvider(resource=resource)
    provider.add_span_processor(BatchSpanProcessor(exporter))
    trace.set_tracer_provider(provider)

    Instrumentator().instrument(app).expose(app)
    RequestsInstrumentor().instrument()
    LoggingInstrumentor().instrument(set_logging_format=True)
    FastAPIInstrumentor().instrument_app(app)


def get_trace_provider():
    return trace.get_tracer_provider()


def trace_method(func):
    def wrapper(*args, **kwargs):
        tracer = get_trace_provider().get_tracer(__name__)
        with tracer.start_as_current_span(func.__name__):
            return func(*args, **kwargs)

    return wrapper
