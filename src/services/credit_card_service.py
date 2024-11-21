from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config
import streamlit as st


def analyze_credit_card(card_url):
    try:
        credential = AzureKeyCredential(Config.AZURE_DOCUMENT_INTELLIGENCE_KEY)
        document_client = DocumentIntelligenceClient(Config.AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT, credential)

        card_info = document_client.begin_analyze_document(
            "prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url)
        )
        result = card_info.result()

       

        for document in result.documents:
            fields = document.get('fields', {})

            return {
                "card_name": fields.get('CardHolderName', {}).get('content'),
                "card_number": fields.get('CardNumber', {}).get('content'),
                "expiry_date": fields.get('ExpirationDate', {}).get('content'),
                "bank_name": fields.get('IssuingBank', {}).get('content'),
            }
    except Exception as ex:
        st.error(f"Erro ao analisar cartão de crédito: {ex}")
        return None

