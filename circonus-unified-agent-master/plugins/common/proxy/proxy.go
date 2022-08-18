package proxy

import (
	"fmt"
	"net/http"
	"net/url"
)

type HTTPProxy struct {
	HTTPProxyURL string `toml:"http_proxy_url"`
}

type ProxyFunc func(req *http.Request) (*url.URL, error) //nolint:golint

func (p *HTTPProxy) Proxy() (ProxyFunc, error) {
	if len(p.HTTPProxyURL) > 0 {
		url, err := url.Parse(p.HTTPProxyURL)
		if err != nil {
			return nil, fmt.Errorf("error parsing proxy url %q: %w", p.HTTPProxyURL, err)
		}
		return http.ProxyURL(url), nil
	}
	return http.ProxyFromEnvironment, nil
}