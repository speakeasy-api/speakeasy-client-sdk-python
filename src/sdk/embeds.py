import requests
from . import utils
from sdk.models import operations, shared
from typing import Optional

class Embeds:
    _client: requests.Session
    _security_client: requests.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests.Session, security_client: requests.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version

    
    def get_embed_access_token(self, request: operations.GetEmbedAccessTokenRequest) -> operations.GetEmbedAccessTokenResponse:
        r"""Get an embed access token for the current workspace.
        Returns an embed access token for the current workspace. This can be used to authenticate access to externally embedded content.
        Filters can be applied allowing views to be filtered to things like particular customerIds.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/workspace/embed-access-token"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetEmbedAccessTokenResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.EmbedAccessTokenResponse])
                res.embed_access_token_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_valid_embed_access_tokens(self) -> operations.GetValidEmbedAccessTokensResponse:
        r"""Get all valid embed access tokens for the current workspace.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/workspace/embed-access-tokens/valid"
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetValidEmbedAccessTokensResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[shared.EmbedToken]])
                res.embed_tokens = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def revoke_embed_access_token(self, request: operations.RevokeEmbedAccessTokenRequest) -> operations.RevokeEmbedAccessTokenResponse:
        r"""Revoke an embed access EmbedToken.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/workspace/embed-access-tokens/{tokenID}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.RevokeEmbedAccessTokenResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    