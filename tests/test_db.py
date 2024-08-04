import pandas as pd
from extract.db import get_data


def test_get_data():
    df, partitons = get_data(load_dt="20150101", movie_type={"multiMovieYn": "N"})
    assert isinstance(df, pd.DataFrame)
    assert isinstance(partitons, list)