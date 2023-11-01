int tsub_ok(int x, int y)
{
    if (y == 0) // no overflow possible
        return 1;
    else if (x == INT_MIN && y == -1) // if x is smallest and subtract 1 then overflow
        return 0;
    else
        return x - y >= 0; // if greater than 0 then there is no overflow but otherwise there is
}

((x & 0xFF) | (y & ~0xFF))

    int is_little_endian()
{
    uint32_t i = 1;
    char *c = (char *)&i;
    return c[0] == 1;
}
