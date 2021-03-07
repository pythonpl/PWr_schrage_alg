// IMPORT Z REPOZYTORIUM NA BITBUCKET

Sprawozdanie: Podejście sortR vs Algorytm Schrage'a

Podejście sortR uwzględnia w ustalaniu kolejności jedynie czas przygotowania zadania (parametr r), naiwnie licząc, że im szybciej zadanie zostanie uruchomione, tym szybciej zostanie dostarczone. W podejściu Algorytmu Schrage'a również zaczyna się od ustalenia tego, które zadanie będzie szybciej można poddać wykonaniu, jednak bierze się pod uwagę także drugi parametr - czas wykonania. W kolejce jako pierwsze zostają umieszczone zadania o krótkim czasie przygotowania, ale długim czasie wykonania. Podejście to jest o tyle racjonalne, że zadania o większym parametrze r mają czas by zostać przygotowane (w czasie gdy i tak nie mogą trafić na maszynę, bo wykonują się poprzednie zadania), i potem z jak najmniejszym okresem bezczynności maszyny zostać wykonane. 
