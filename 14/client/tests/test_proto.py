from proto import Request, Response, Op, Status


def test_request_pack_unpack() -> None:
    """Test that Request.pack and Request.unpack are consistent."""
    req = Request(
        user_id=12345,
        version=1,
        op=Op.Save,
        filename="test.txt",
        payload=b"Hello, world!"
    )
    packed: bytes = req.pack()
    unpacked: Request = Request.unpack(packed)

    assert unpacked.user_id == req.user_id
    assert unpacked.version == req.version
    assert unpacked.op == req.op
    assert unpacked.filename == req.filename
    assert unpacked.payload == req.payload


def test_response_pack_unpack() -> None:
    """Test that Response.pack and Response.unpack are consistent."""
    res = Response(
        version=1,
        status=Status.SuccessRetrieved,
        filename="test.txt",
        payload=b"Hello, world!"
    )
    packed: bytes = res.pack()
    unpacked: Response = Response.unpack(packed)

    assert unpacked.version == res.version
    assert unpacked.status == res.status
    assert unpacked.filename == res.filename
    assert unpacked.payload == res.payload
