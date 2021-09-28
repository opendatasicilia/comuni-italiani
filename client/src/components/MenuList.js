import React from "react";
import { FixedSizeList as List } from "react-window";

const OPTION_HEIGHT = 40;
const ROWS = 6;

const MenuList = ({
  options,
  children,
  getValue
}) => {
  const [value] = getValue();
  const initialOffset =
    options.indexOf(value) !== -1
      ? Array.isArray(children) &&
        children.length >= ROWS
        ? options.indexOf(value) >= ROWS
          ? options.indexOf(value) *
              OPTION_HEIGHT -
            OPTION_HEIGHT * 5
          : 0
        : 0
      : 0;

  return Array.isArray(children) ? (
    <List
      height={
        children.length >= ROWS
          ? OPTION_HEIGHT * ROWS
          : children.length * OPTION_HEIGHT
      }
      itemCount={children.length}
      itemSize={OPTION_HEIGHT}
      initialScrollOffset={initialOffset}
    >
      {({ style, index }) => {
        return (
          <div style={style}>
            {children[index]}
          </div>
        );
      }}
    </List>
  ) : (
    <div>{children}</div>
  );
};

export default MenuList;