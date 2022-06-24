

  // 函数a相关代码
  // function a(a => 16) {
  //       var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
  //       // 循环了16次
  //       for (d = 0; a > d; d += 1)
  //           e = Math.random() * b.length,
  //           e = Math.floor(e),
  //           c += b.charAt(e);
  //       return c
  //   }

  !function() {
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    // AES加密 16位AES 填充值保证密钥长度=16位   iv值：”0102030405060708“ AES采用 CBC加密模式
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        //  处理
        return setMaxDigits(131),
        //   RSA再次加密 非对称加密
        d = new RSAKeyPair(b,"",c),
        //   处理
        e = encryptedString(d, a)
    }
    function RSAKeyPair(a, b, c) {
        this.e = biFromHex(a),
        this.d = biFromHex(b),
        this.m = biFromHex(c),
        this.chunkSize = 2 * biHighIndex(this.m),
        this.radix = 16,
        this.barrett = new BarrettMu(this.m)
    }
    function biFromHex(a) {
        var d, e, b = new BigInt, c = a.length;
        for (d = c, e = 0; d > 0; d -= 4, ++e)
        b.digits[e] = hexToDigit(a.substr(Math.max(d - 4, 0), Math.min(d, 4)));
        return b
    }

    function BarrettMu(a) {
        this.modulus = biCopy(a),
        this.k = biHighIndex(this.modulus) + 1;
        var b = new BigInt;
        b.digits[2 * this.k] = 1,
        this.mu = biDivide(b, this.modulus),
        this.bkplus1 = new BigInt,
        this.bkplus1.digits[this.k + 1] = 1,
        this.modulo = BarrettMu_modulo,
        this.multiplyMod = BarrettMu_multiplyMod,
        this.powMod = BarrettMu_powMod
    }


    function setMaxDigits(a >= 131) {
        maxDigits = a, // 131 => MaxDigits
        ZERO_ARRAY = new Array(maxDigits); // 131 数组
        // 131次
        for (var b = 0; b < ZERO_ARRAY.length; b++)
        ZERO_ARRAY[b] = 0;
        bigZero = new BigInt,
        bigOne = new BigInt,
        bigOne.digits[0] = 1
    }

    function BigInt(a) {
        this.digits = "boolean" == typeof a && 1 == a ? null : ZERO_ARRAY.slice(0),
        this.isNeg = !1
    }

    function encryptedString(a, b) {
        for (var f, g, h, i, j, k, l, c = new Array, d = b.length, e = 0; d > e; )
        c[e] = b.charCodeAt(e),
        e++;
        for (; 0 != c.length % a.chunkSize; )
        c[e++] = 0;
        for (f = c.length,
        g = "",
        e = 0; f > e; e += a.chunkSize) {
        for (j = new BigInt,
        h = 0,
        i = e; i < e + a.chunkSize; ++h)
            j.digits[h] = c[i++],
            j.digits[h] += c[i++] << 8;
        k = a.barrett.powMod(j, a.e),
        l = 16 == a.radix ? biToHex(k) : biToString(k, a.radix),
        g += l + " "
        }
    return g.substring(0, g.length - 1)
    }

    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        //   第二次加密  第一次加密的内容， i（随机16字符串）再次加密
        h.encText = b(h.encText, i),
        //   encSecKey 加密
        //   公共密钥 -> 变成字节 16进制 （幂次方计算 长度）
        h.encSecKey = c(i, e, f),
        h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
    window.asrsea = d,
    window.ecnonasr = e
}();