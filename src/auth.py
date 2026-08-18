"""OAuth token management for Meridian connectors."""

TOKEN_REFRESH_MARGIN_SECONDS = 300

def get_valid_token(credentials):
    """Return a valid access token, refreshing it if it's close to expiry."""
    if credentials.expires_in() < TOKEN_REFRESH_MARGIN_SECONDS:
        credentials = refresh_token(credentials)
    return credentials.access_token

def refresh_token(credentials):
    """Exchange the refresh token for a new access token."""
    response = oauth_client.refresh(credentials.refresh_token)
    return Credentials(response.access_token, response.refresh_token, response.expires_in)
