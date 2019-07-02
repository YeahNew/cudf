# Copyright (c) 2019, NVIDIA CORPORATION.

import cudf
import pytest
from dask.dataframe.utils import is_dataframe_like  # noqa: E402
from dask.dataframe.utils import is_index_like, is_series_like

dask = pytest.importorskip(
    "dask",
    minversion="1.1.0",
    reason="Needs Dask 1.1.0+ to use `is_dataframe_like`",
)


def test_is_dataframe_like():
    df = cudf.DataFrame({"x": [1, 2, 3]})
    assert is_dataframe_like(df)
    assert is_series_like(df.x)
    assert is_index_like(df.index)
    assert not is_dataframe_like(df.x)
    assert not is_series_like(df)
    assert not is_index_like(df)
