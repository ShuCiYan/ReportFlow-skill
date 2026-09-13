# Search Adapter and Fallback

AnySearch is optional. Record provider status as `IMPLEMENTED`, `AVAILABLE`, `UNAVAILABLE`, or `DOCUMENTED ONLY`. Provider failure (DNS, timeout, unavailable service, extraction failure, inaccessible page, duplicate result, unavailable original) is logged and routed to the next provider; it never lowers evidence standards or silently becomes a zero-result search.

Before designing a custom framework, check Existing Project Knowledge → Model Library → Knowledge Base → available skills → Web/Search Provider. Custom methods are marked `experimental/custom` with a reason.
