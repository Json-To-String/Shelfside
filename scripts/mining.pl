use LWP::Simple;

my $url = "http://www.boardgamegeek.com/browse/boardgame";
my $content = get $url; # Gets the HTML page.
if (defined $content)
  {
  # Do something with content (which is the returned HTML) here.
  }