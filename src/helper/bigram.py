
import string

punct = set(u''':!),.:;?]}¢'"、。〉》」』】〕】〞︰︱︳﹐､﹒
            ﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠
            々∥•‧ˇˉ─--′』」([{£¥'"‵〈《「『【〔【（［｛￡￥〝︵︷︹︻
            ︽︿﹁﹃﹙﹛﹝（｛「『-—_…''')

punct.union( string.punctuation )
punct.union( string.whitespace )

def get_words( text ):
    pure_text = '^'+''.join( w if w not in punct else ' ' for w in text )+'$'
    raw_words = []
    for i in range( 1 , len( pure_text ) ):
        raw_words.append( pure_text[ i-1:i+1 ] )
    res = " ".join( raw_words )
    res = res.replace( '\n' , '' )
    res = res.replace( '\r' , '' )
    res = res.replace( '\\n' , '' )
    res = res.replace( '\\r' , '' )
    return res

