import streamlit as slt

# -----------------
# Import the CSS file bc i like it organized
# -----------------

with open("static/index.css") as f:
    css = f.read()

# -----------------

slt.html(
f"""
<style>{css}</style>
<div class="spacer">

</div>
"""
)

#slt.image("./static/the-wall.png")

slt.title("Home")
slt.write(
    """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus finibus eleifend pharetra. Pellentesque volutpat, ipsum id volutpat porta, ligula diam dapibus velit, auctor fringilla quam tortor a est. Aliquam a mi ornare justo tincidunt commodo. Vivamus vitae tellus aliquet, lacinia nunc vitae, congue diam. Praesent venenatis molestie venenatis. Proin varius, nulla non molestie efficitur, tortor augue eleifend nisl, nec vehicula ligula dolor ullamcorper augue. Nam pharetra mi sit amet augue egestas, sed efficitur lectus congue. Maecenas sem velit, hendrerit at ultricies et, egestas et nisl. Ut ornare, massa et tincidunt tempus, dolor ipsum pulvinar nisl, sit amet efficitur nunc erat a dui. Sed orci ligula, imperdiet eget dictum at, suscipit eget justo. Fusce eleifend viverra augue sed tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vivamus elementum elit sit amet venenatis tincidunt.

Nam tristique feugiat dictum. Nam dignissim metus massa, eu tempus nibh maximus vel. Nulla in vestibulum elit. Cras mollis lorem in magna ultrices, a pharetra leo pharetra. Aliquam erat volutpat. Aenean purus lorem, sodales a metus sed, vehicula feugiat nisl. Proin sed erat luctus, rhoncus dui quis, finibus velit. Proin vitae viverra lacus.

Sed dapibus placerat commodo. Curabitur elit metus, eleifend sed semper in, hendrerit vitae turpis. Nulla augue metus, aliquet vel pretium eu, pretium vitae velit. Donec nec nisl mattis, pretium turpis nec, mollis metus. In ut semper elit. Praesent ullamcorper rutrum pellentesque. Ut efficitur lorem ac tortor tincidunt, id suscipit orci feugiat. Aliquam neque urna, ornare non laoreet quis, consequat ac erat. Quisque venenatis dictum massa dignissim facilisis.

Morbi lorem est, malesuada blandit leo rhoncus, maximus faucibus urna. Nam efficitur urna ut metus iaculis molestie. Vivamus nec lacus ut felis malesuada mollis at sit amet ex. Sed tincidunt dui dui, eget sodales turpis commodo cursus. Donec ut venenatis diam. Curabitur nulla nibh, feugiat eleifend mollis a, efficitur ac nibh. Duis non est vestibulum, bibendum orci non, lacinia eros. Donec a est a est posuere congue. Vestibulum convallis ornare turpis. Sed volutpat pharetra magna, aliquet feugiat nibh ornare ultrices.

Integer quis mattis lorem, eu dapibus tortor. Nullam volutpat nibh at laoreet tristique. Fusce tortor justo, efficitur nec pharetra sed, auctor semper augue. Nunc ac suscipit mi. Pellentesque id felis diam. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Proin mi risus, mollis in mauris a, luctus venenatis ipsum. Nullam posuere eros at lobortis pharetra. Integer ut lacus eget lectus vehicula tempus. Ut blandit urna diam, convallis consectetur tortor efficitur sit amet. Nunc tempus scelerisque diam, ac pulvinar ex facilisis at. Mauris interdum cursus urna in blandit."""
)