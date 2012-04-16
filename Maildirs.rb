# Maildirs sublet file
# Created with sur-0.2
configure :Maildirs do |s|
  s.interval = s.config[:interval] || 60

  s.icon = Subtlext::Icon.new("mail.xbm")
  s.label = s.config[:label] || 'Mail'
  s.dirmap = s.config[:dirmap]
end

on :run do |s|
  s.data = s.icon + ' ' + s.label + ' ' + s.dirmap.map do |prefix, dir|
    prefix + ' ' + (Dir.entries(dir).size - 2).to_s
  end.join(" | ")
end
