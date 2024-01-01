import json
import os
from typing import Any, Dict, List

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CheckGpuSerializer, XyGraphSerializer

# Create your views here.


class SampleAPIView(APIView):
    def get(self, request: Request) -> Response:
        return Response("OK !!", status=status.HTTP_200_OK)


def parse_json_log(logpath: str, req_type: str) -> List[Dict[str, Any]]:
    ps_log: List[Dict[str, Any]] = []
    with open(logpath, "r") as file:
        for line in file:
            log_entry = json.loads(line)
            if log_entry["tag"] == req_type:
                ps_log.append(log_entry)

    return ps_log


class XyGraphAPIView(APIView):
    def get(self, request: Request) -> Response:
        logpath = os.environ.get("LOG_PATH")
        if logpath is None:
            return Response(
                data={"error": "LOG_PATH environment variable not set"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        ps_log = parse_json_log(logpath, req_type="xy")

        serializer = XyGraphSerializer(data=ps_log, many=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)


class CheckGpuAPIView(APIView):
    def get(self, request: Request) -> Response:
        logpath = os.environ.get("LOG_PATH")
        if logpath is None:
            return Response(
                data={"error": "LOG_PATH environment variable not set"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        ps_log = parse_json_log(logpath, req_type="gpu")

        serializer = CheckGpuSerializer(data=ps_log, many=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)


# views.py
def index(request: Request) -> HttpResponse:
    return render(request, "index.html")
