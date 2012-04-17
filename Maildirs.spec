# -*- encoding: utf-8 -*-
# Maildirs specification file
# Created with sur-0.2
Sur::Specification.new do |s|
  # Sublet information
  s.name        = "Maildirs"
  s.version     = "0.2"
  s.tags        = [ "Mail", "Icon" ]
  s.files       = [ "Maildirs.rb" ]
  s.icons       = [ "icons/mail.xbm" ]

  # Sublet description
  s.description = "Display unread mailcount in specified Maildirs"
  s.notes       = <<NOTES
This sublet displays the number of unread mails in Maildirs specified.
NOTES

  # Sublet authors
  s.authors     = [ "gattuso" ]
  s.contact     = "null@gmx.it"
  s.date        = "Mon Apr 16 19:15 CEST 2012"

  # Sublet config
  s.config = [
    {
      :name        => "dirmap",
      :type        => "Hashmap",
      :description => "This is an Hashmap specifing the prefix for the key and the suffix for the value",
      :def_value   => "Hash.new"
    }
  ]

  # Sublet grabs
  #s.grabs = {
  #  :MaildirsGrab => "Sublet grab"
  #}

  # Sublet requirements
  # s.required_version = "0.9.2127"
  # s.add_dependency("subtle", "~> 0.1.2")
end
