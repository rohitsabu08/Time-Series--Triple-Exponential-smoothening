# Time-Series--Triple-Exponential-smoothening

When the data shows Level (L), trend (b), seasonality (s), frequency of seasons (m) we use TES
Also Known as Holts winter Exponential Smoothening

In TES, Alpha, beta and gamma are the smoothing parameters

There are two approaches to TES based on how the Level, Trend and Seasonal components are combined to produce the forecast

1. Additive: add up the L + T + S

2. Multiplicative L * T * S or [L + T] * S
